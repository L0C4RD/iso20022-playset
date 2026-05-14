from . import base_types
from ._Max210Text import Max210Text
from ._PartyIdentification272 import PartyIdentification272
from ._PaymentMethod3Choice import PaymentMethod3Choice

class InvoiceLegalIssue5(base_types._BaseFieldType):

	__slots__ = ["_InvcLglStmt", "_Invcee", "_Invcr", "_PmtMtd"]
	@property
	def InvcLglStmt(self):
		return self._InvcLglStmt

	@InvcLglStmt.setter
	def InvcLglStmt(self, value):
		self._InvcLglStmt = value if type(value) != base_types.auto else self.make_default("InvcLglStmt")

	@InvcLglStmt.deleter
	def InvcLglStmt(self):
		del self._InvcLglStmt
		self._InvcLglStmt = None

	@property
	def Invcee(self):
		return self._Invcee

	@Invcee.setter
	def Invcee(self, value):
		self._Invcee = value if type(value) != base_types.auto else self.make_default("Invcee")

	@Invcee.deleter
	def Invcee(self):
		del self._Invcee
		self._Invcee = None

	@property
	def Invcr(self):
		return self._Invcr

	@Invcr.setter
	def Invcr(self, value):
		self._Invcr = value if type(value) != base_types.auto else self.make_default("Invcr")

	@Invcr.deleter
	def Invcr(self):
		del self._Invcr
		self._Invcr = None

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if type(value) != base_types.auto else self.make_default("PmtMtd")

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvcLglStmt', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcee', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=PaymentMethod3Choice, min=0, max=1, mutex_group=None, array=False),
	))

