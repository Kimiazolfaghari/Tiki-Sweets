export default function SubmitButton({ text }) {
    return (
      <button
        type="submit"
        className="w-full bg-rose-300 hover:bg-rose-400 text-white font-bold py-3 px-4 rounded-xl mt-4 transition"
      >
        {text}
      </button>
    );
  }
  