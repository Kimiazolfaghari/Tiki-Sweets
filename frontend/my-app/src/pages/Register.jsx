import { useState } from "react";

export default function Register() {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    username: "",
    password: "",
    phone: "",
    email: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData); // بعداً وصلش می‌کنیم به API
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gradient-to-r from-amber-100 to-rose-100 px-4">
      <form
        onSubmit={handleSubmit}
        className="bg-white bg-opacity-70 rounded-3xl shadow-2xl p-10 w-full max-w-md"
      >
        <h2 className="text-2xl font-bold text-center text-gray-800">
          Account Sign Up
        </h2>
        <p className="text-center text-sm text-gray-500 mb-6">Create Account</p>

        <input
          type="text"
          name="firstName"
          placeholder="First Name"
          value={formData.firstName}
          onChange={handleChange}
          className="w-full p-3 mb-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-rose-300"
        />
        <input
          type="text"
          name="lastName"
          placeholder="Last Name"
          value={formData.lastName}
          onChange={handleChange}
          className="w-full p-3 mb-3 border border-gray-300 rounded-xl"
        />
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          className="w-full p-3 mb-3 border border-gray-300 rounded-xl"
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          className="w-full p-3 mb-3 border border-gray-300 rounded-xl"
        />
        <input
          type="text"
          name="phone"
          placeholder="Phone Number"
          value={formData.phone}
          onChange={handleChange}
          className="w-full p-3 mb-3 border border-gray-300 rounded-xl"
        />
        <input
          type="email"
          name="email"
          placeholder="Email Address"
          value={formData.email}
          onChange={handleChange}
          className="w-full p-3 mb-4 border border-gray-300 rounded-xl"
        />

        <button
          type="submit"
          className="w-full bg-rose-300 hover:bg-rose-400 text-white font-semibold py-3 rounded-xl transition duration-300"
        >
          Sign Up
        </button>

        <p className="mt-4 text-center text-sm text-gray-600">
          Already Have An Account?{" "}
          <a
            href="/login"
            className="text-rose-500 font-semibold hover:underline"
          >
            Log In
          </a>
        </p>
      </form>
    </div>
  );
}
