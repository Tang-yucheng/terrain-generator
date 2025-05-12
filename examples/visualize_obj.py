import open3d as o3d
import os

# 设置路径
# folder_path = "results/mountains"
# filenames = ["mountain.obj"]

# folder_path = "results/primitive_separated/generate_floating_box_grid"
# folder_path = "results/primitive_separated/generate_floating_box_grid_slope"
# filenames = ["mesh_0.0_floating.obj", "mesh_0.0.obj", "mesh_1.0_floating.obj", "mesh_1.0.obj"]

folder_path = "results/generated_terrain/mesh_0"
filenames = ["mesh.obj"]

# 加载所有 mesh
meshes = []
for fname in filenames:
    mesh_path = os.path.join(folder_path, fname)
    mesh = o3d.io.read_triangle_mesh(mesh_path)
    mesh.compute_vertex_normals()
    meshes.append(mesh)

# # 显示
# o3d.visualization.draw_geometries(meshes)

# 创建可视化器
vis = o3d.visualization.Visualizer()
vis.create_window()
for mesh in meshes:
    vis.add_geometry(mesh)

# 获取视角控制器
ctr = vis.get_view_control()

# 设置相机参数（关键）
ctr.set_lookat([5, 5, 0])            # 相机观察的目标点
ctr.set_up([0, 0, 1])                # 相机的上方向（默认 Y 向上）
ctr.set_front([1, 1, 1])             # 相机的朝向（单位向量）
ctr.set_zoom(0.5)                    # 缩放程度，越小越远（默认 0.7）

# 渲染窗口
vis.run()
vis.destroy_window()
