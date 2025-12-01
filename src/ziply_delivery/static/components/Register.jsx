import React, { useState } from "react";
import "./Register.css";

function Register() {
  // state for demo errors & status
  const [errors, setErrors] = useState({});
  const [status, setStatus] = useState("");

  // small validator that sets aria states
  function validateAndSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const email = form["reg-email"].value.trim();
    const first = form["reg-first-name"].value.trim();
    const last = form["reg-last-name"].value.trim();
    const phone = form["reg-phone"].value.trim();
    const pass = form["reg-password"].value;
    const pass2 = form["reg-confirm"].value;

    const nextErrors = {};

    if (!email || !/^\S+@\S+\.\S+$/.test(email)) {
      nextErrors.email = "Please enter a valid email";
    }
    if (!first) nextErrors.first = "First name required";
    if (!last) nextErrors.last = "Last name required";
    if (!phone) nextErrors.phone = "Phone required";
    if (!pass) nextErrors.password = "Password required";
    if (pass && pass !== pass2) nextErrors.confirm = "Passwords do not match";

    setErrors(nextErrors);

    // if no errors, show success and clear errors
    if (Object.keys(nextErrors).length === 0) {
      setStatus("Registration submitted successfully.");
      setTimeout(() => setStatus(""), 3000); // emulate sending form
      form.reset();
    } else {
      setStatus("There are errors in the form.");
    }
  }

  return (
    <div className="auth-card" aria-live="polite">
      {/* heading has id so form can reference it */}
      <h2 id="register-title">Create Your Ziply Account</h2>
      <p id="register-sub" className="subtitle">
        Fill out the form below to get started
      </p>

      {/* form: native element and accessible name via aria-labelledby */}
      <form
        onSubmit={validateAndSubmit}
        aria-labelledby="register-title"
        aria-describedby="register-sub"
      >
        {/* Email */}
        <div className="form-group">
          <label className="form-label" htmlFor="reg-email">
            Email Address
          </label>
          <input
            className="input-field"
            id="reg-email"
            name="reg-email"
            type="email"
            required
            aria-required="true"
            aria-invalid={errors.email ? "true" : "false"}
            aria-errormessage={errors.email ? "err-email" : undefined}
            aria-describedby={errors.email ? "err-email" : undefined}
          />
          {/* error span — role="alert" will be announced immediately by many screen readers */}
          {errors.email && (
            <div id="err-email" role="alert" className="sr-only">
              {errors.email}
            </div>
          )}
        </div>

        {/* First + Last */}
        <div className="form-row">
          <div className="form-group" style={{ flex: 1 }}>
            <label className="form-label" htmlFor="reg-first-name">
              First Name
            </label>
            <input
              className="input-field"
              id="reg-first-name"
              name="reg-first-name"
              type="text"
              required
              aria-required="true"
              aria-invalid={errors.first ? "true" : "false"}
              aria-errormessage={errors.first ? "err-first" : undefined}
            />
            {errors.first && (
              <div id="err-first" role="alert" className="sr-only">
                {errors.first}
              </div>
            )}
          </div>

          <div className="form-group" style={{ flex: 1 }}>
            <label className="form-label" htmlFor="reg-last-name">
              Last Name
            </label>
            <input
              className="input-field"
              id="reg-last-name"
              name="reg-last-name"
              type="text"
              required
              aria-required="true"
              aria-invalid={errors.last ? "true" : "false"}
              aria-errormessage={errors.last ? "err-last" : undefined}
            />
            {errors.last && (
              <div id="err-last" role="alert" className="sr-only">
                {errors.last}
              </div>
            )}
          </div>
        </div>

        {/* Phone */}
        <div className="form-group">
          <label className="form-label" htmlFor="reg-phone">
            Telephone Number
          </label>
          <input
            className="input-field"
            id="reg-phone"
            name="reg-phone"
            type="tel"
            required
            aria-required="true"
            aria-invalid={errors.phone ? "true" : "false"}
            aria-errormessage={errors.phone ? "err-phone" : undefined}
          />
          {errors.phone && (
            <div id="err-phone" role="alert" className="sr-only">
              {errors.phone}
            </div>
          )}
        </div>

        {/* Password */}
        <div className="form-group">
          <label className="form-label" htmlFor="reg-password">
            Password
          </label>
          <input
            className="input-field"
            id="reg-password"
            name="reg-password"
            type="password"
            required
            aria-required="true"
            aria-invalid={errors.password ? "true" : "false"}
            aria-errormessage={errors.password ? "err-password" : undefined}
          />
          {errors.password && (
            <div id="err-password" role="alert" className="sr-only">
              {errors.password}
            </div>
          )}
        </div>

        {/* Confirm Password */}
        <div className="form-group">
          <label className="form-label" htmlFor="reg-confirm">
            Confirm Password
          </label>
          <input
            className="input-field"
            id="reg-confirm"
            name="reg-confirm"
            type="password"
            required
            aria-required="true"
            aria-invalid={errors.confirm ? "true" : "false"}
            aria-errormessage={errors.confirm ? "err-confirm" : undefined}
          />
          {errors.confirm && (
            <div id="err-confirm" role="alert" className="sr-only">
              {errors.confirm}
            </div>
          )}
        </div>

        <button
          type="submit"
          className="btn btn-primary"
          style={{ width: "100%", marginTop: "1rem" }}
          aria-label="Create Account"
        >
          Create Account
        </button>
      </form>

      {/* status area — role=status is polite and not disruptive */}
      <div
        id="form-status"
        role="status"
        aria-live="polite"
        className="center"
        style={{ marginTop: "1rem" }}
      >
        {status}
      </div>

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
