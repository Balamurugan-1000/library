 # TODO – Library App

This file tracks feature-level progress.
Each feature should be developed via a dedicated PR
(models → views → templates → manual verification).

---

## ✅ Completed
- [x] Create project and core apps
- [x] Define base models (User, Book, Borrowing)
- [x] Admin registration and migrations
- [x] Migrate DB from sqlite to postgres
- [x] Feature: Authentication (Login / Logout)

---

## 📚 Feature: Book Listing (Read-only)

**Goal:** allow users to view library inventory

- [ ] Add available copies calculation to `Book` model
- [ ] Create authenticated book list view
- [ ] Create book list template
- [ ] Display title, author, total copies, available copies
- [ ] Ensure listing is read-only (no actions yet)

---

## 👥 Feature: User Roles (Librarian vs User)

**Goal:** prepare permission system

- [ ] Decide how librarian role is assigned (admin-only)
- [ ] Add role-check helper for librarian
- [ ] Restrict librarian-only actions in code (no UI yet)
- [ ] Verify role logic via admin and shell

---

## 🔄 Feature: Rent Book – Request Flow (User)

**Goal:** allow users to request renting a book

- [ ] Block request if no copies available
- [ ] Block duplicate active borrowing per user/book
- [ ] Create rent request view
- [ ] Create minimal rent request button/template
- [ ] Create borrowing record with `PENDING_RENT` status

---

## ✅ Feature: Rent Book – Approval Flow (Librarian)

**Goal:** librarian controls final renting

- [ ] List pending rent requests (librarian only)
- [ ] Approve rent request (status → RENTED)
- [ ] Reject rent request (status → REJECTED)
- [ ] Reduce availability only on approval
- [ ] Prevent invalid state transitions

---

## 🔁 Feature: Return Book – Request Flow (User)

**Goal:** allow users to initiate return

- [ ] Allow return request for rented books
- [ ] Change status to `PENDING_RETURN`
- [ ] Ensure only active rentals can be returned

---

## 🔁 Feature: Return Book – Approval Flow (Librarian)

**Goal:** librarian finalizes return

- [ ] List pending return requests
- [ ] Approve return (status → RETURNED)
- [ ] Reject return (status remains RENTED)
- [ ] Restore availability only on approval

---

## 🧠 Feature: Business Rules Hardening

**Goal:** make illegal states impossible

- [ ] Validate borrowing state transitions centrally
- [ ] Enforce one active borrowing per user per book
- [ ] Add defensive checks at model/service level
- [ ] Add admin warnings for invalid actions

---

## 🔌 Feature: API Layer (Later)

**Goal:** support CLI and future clients

- [ ] Authenticated rent request API
- [ ] Librarian approval APIs
- [ ] Return flow APIs
- [ ] Token-based auth for CLI usage

---

## 🧪 Feature: Polish & Safety (Optional)

- [ ] Manual end-to-end testing
- [ ] Add basic unit tests for rules
- [ ] Improve admin UX
- [ ] Update README with usage instructions

---

## 📌 Rules
- One feature = one PR
- No vague commits
- No API before core logic is stable
- Update this file in every PR
