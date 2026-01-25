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

## 📚 Feature: Book Listing with Search & Filters

**Goal:** allow users to view and discover books

- [ ] Add available copies calculation to `Book` model
- [ ] Create authenticated book list view
- [ ] Create book list template with search bar
- [ ] Display title, author, total copies, available copies
- [ ] Add search functionality (title/author search)
- [ ] Add filters (availability, genre)
- [ ] Implement Django Q objects for complex queries
- [ ] Add pagination for large book lists

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

## 🖼️ Feature: Book Management & Files

**Goal:** handle book covers and bulk operations

- [ ] Add cover image upload to Book model
- [ ] Configure media files handling
- [ ] Create book creation/editing forms
- [ ] Implement CSV import for bulk books
- [ ] Add book cover display in listings
- [ ] Handle image validation and resizing

---

## 📧 Feature: Email Notifications System

**Goal:** automated communication with users

- [ ] Configure Django email backend
- [ ] Create email templates for borrowing status
- [ ] Implement email sending on status changes
- [ ] Add email preferences to user profile
- [ ] Test email delivery (development + production)

---

## 🔌 Feature: REST API Layer

**Goal:** support mobile/cli integration

- [ ] Install Django REST Framework
- [ ] Create API serializers for Book/Borrowing
- [ ] Implement token authentication
- [ ] Build endpoints for rent/return flows
- [ ] Add API documentation (Swagger)

---

## ⚡ Feature: Background Tasks & Analytics

**Goal:** automation and insights

- [ ] Set up Celery with Redis
- [ ] Create overdue book checking task
- [ ] Implement borrowing analytics
- [ ] Build dashboard for trends
- [ ] Add penalty calculation system
- [ ] Schedule regular maintenance tasks

---

## 🧪 Feature: Testing & Production Ready

- [ ] Write unit tests for core business logic
- [ ] Add integration tests for API endpoints
- [ ] Set up test database and fixtures
- [ ] Configure CI/CD pipeline
- [ ] Add environment-specific settings
- [ ] Implement logging and monitoring
- [ ] Write comprehensive README

---

## 📌 Rules
- One feature = one PR
- No vague commits
- Update this file in every PR
