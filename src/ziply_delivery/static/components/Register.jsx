import "./Register.css";

function Register() {
  return (
    <div className="auth-card">
      <h2>Create Your Ziply Account</h2>
      <p className="subtitle">Fill out the form below to get started</p>

      <form
        aria-label="Registration Form"
        onSubmit={(e) => {
          e.preventDefault();
          alert("Registration submitted!");
        }}
      >
        {/* form fields here */}
      </form>

      <div style={{ textAlign: "center", marginTop: "1.5rem" }}>
        <button
          className="switch-link"
          aria-label="Go to Login Page"
          onClick={() => (window.location.href = "/login")}
        >
          Already have an account? Log in
        </button>
      </div>
    </div>
  );
}

export default Register;