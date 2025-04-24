import { createBrowserRouter, RouterProvider, Navigate } from "react-router-dom";
import Register from "./pages/Register";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/register" replace />,
    errorElement: (
      <div className="text-center text-red-500 text-xl mt-20">
        ❌ مسیر پیدا نشد (404)
      </div>
    ),
  },
  {
    path: "/register",
    element: <Register />,
  },
]);

export default function AppRouter() {
  return <RouterProvider router={router} />;
}
