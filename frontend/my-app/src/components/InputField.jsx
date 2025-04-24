export default function InputField({ type = "text", placeholder, name, value, onChange }) {
    return (
      <input
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className="w-full p-3 my-2 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-rose-300"
      />
    );
  }
  