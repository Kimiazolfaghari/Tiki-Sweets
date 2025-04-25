import React from 'react';

const VerifyAccount = () => {
  return (
    <div className="card shadow p-4">
      <h2 className="mb-3">تأیید حساب</h2>
      <form>
        <input type="text" placeholder="کد تأیید" className="form-control mb-3" />
        <button className="btn btn-warning w-100">تأیید</button>
      </form>
    </div>
  );
};

export default VerifyAccount;
