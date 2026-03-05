#!/usr/bin/env python3
"""Quick point cloud visualizer for local or remote workflows."""

from __future__ import annotations

import argparse
from pathlib import Path

import open3d as o3d
import plotly.graph_objects as go


DEFAULT_PLY = Path(
    "/home/jatucker/Splat-MOVER/scripts/renders/pcd/gate_bottom_point_cloud.ply"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Visualize a .ply point cloud file.")
    parser.add_argument(
        "ply_path",
        nargs="?",
        default=str(DEFAULT_PLY),
        help=f"Path to .ply file (default: {DEFAULT_PLY})",
    )
    parser.add_argument(
        "--point-size",
        type=float,
        default=2.0,
        help="Rendered point size in pixels (default: 2.0)",
    )
    parser.add_argument(
        "--show-frame",
        action="store_true",
        help="Show XYZ coordinate frame at origin.",
    )
    parser.add_argument(
        "--export-html",
        default="",
        help="Export interactive Plotly HTML (good for remote/headless usage).",
    )
    parser.add_argument(
        "--no-gui",
        action="store_true",
        help="Do not open Open3D GUI window.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ply_path = Path(args.ply_path).expanduser().resolve()

    if not ply_path.exists():
        raise FileNotFoundError(f"Point cloud file not found: {ply_path}")

    pcd = o3d.io.read_point_cloud(str(ply_path))
    if pcd.is_empty():
        raise ValueError(f"Loaded point cloud is empty: {ply_path}")

    geometries = [pcd]
    if args.show_frame:
        geometries.append(
            o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1, origin=[0, 0, 0])
        )

    if args.export_html:
        html_path = Path(args.export_html).expanduser().resolve()
        html_path.parent.mkdir(parents=True, exist_ok=True)
        points = pcd.points
        colors = pcd.colors

        x = [p[0] for p in points]
        y = [p[1] for p in points]
        z = [p[2] for p in points]

        if len(colors) == len(points):
            marker_colors = [
                f"rgb({int(max(0.0, min(1.0, c[0])) * 255)},"
                f"{int(max(0.0, min(1.0, c[1])) * 255)},"
                f"{int(max(0.0, min(1.0, c[2])) * 255)})"
                for c in colors
            ]
        else:
            marker_colors = "royalblue"

        fig = go.Figure(
            data=[
                go.Scatter3d(
                    x=x,
                    y=y,
                    z=z,
                    mode="markers",
                    marker={"size": args.point_size, "color": marker_colors, "opacity": 0.9},
                )
            ]
        )
        fig.update_layout(
            title=f"Point Cloud: {ply_path.name}",
            scene={"xaxis_title": "X", "yaxis_title": "Y", "zaxis_title": "Z"},
            margin={"l": 0, "r": 0, "b": 0, "t": 40},
        )
        fig.write_html(str(html_path), include_plotlyjs="cdn")
        print(f"Saved interactive HTML: {html_path}")

    if not args.no_gui:
        vis = o3d.visualization.Visualizer()
        vis.create_window(window_name=f"Point Cloud: {ply_path.name}")
        for geom in geometries:
            vis.add_geometry(geom)

        render_option = vis.get_render_option()
        if render_option is not None:
            render_option.point_size = args.point_size

        vis.run()
        vis.destroy_window()


if __name__ == "__main__":
    main()
