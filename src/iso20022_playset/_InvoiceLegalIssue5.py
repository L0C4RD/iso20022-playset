# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max210Text
from . import PartyIdentification272
from . import PaymentMethod3Choice

class InvoiceLegalIssue5(base_types._BaseFieldType):

	__slots__ = ["_InvcLglStmt", "_Invcee", "_Invcr", "_PmtMtd"]
	@property
	def InvcLglStmt(self):
		return self._InvcLglStmt

	@InvcLglStmt.setter
	def InvcLglStmt(self, value):
		self._InvcLglStmt = value if value is not None else base_types.UninitialisedField(self, 'InvcLglStmt', Max210Text, False)

	@InvcLglStmt.deleter
	def InvcLglStmt(self):
		del self._InvcLglStmt
		self._InvcLglStmt = base_types.UninitialisedField(self, 'InvcLglStmt', Max210Text, False)

	@property
	def Invcee(self):
		return self._Invcee

	@Invcee.setter
	def Invcee(self, value):
		self._Invcee = value if value is not None else base_types.UninitialisedField(self, 'Invcee', PartyIdentification272, False)

	@Invcee.deleter
	def Invcee(self):
		del self._Invcee
		self._Invcee = base_types.UninitialisedField(self, 'Invcee', PartyIdentification272, False)

	@property
	def Invcr(self):
		return self._Invcr

	@Invcr.setter
	def Invcr(self, value):
		self._Invcr = value if value is not None else base_types.UninitialisedField(self, 'Invcr', PartyIdentification272, False)

	@Invcr.deleter
	def Invcr(self):
		del self._Invcr
		self._Invcr = base_types.UninitialisedField(self, 'Invcr', PartyIdentification272, False)

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtd', PaymentMethod3Choice, False)

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = base_types.UninitialisedField(self, 'PmtMtd', PaymentMethod3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvcLglStmt', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcee', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invcr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=PaymentMethod3Choice, min=0, max=1, mutex_group=None, array=False),
	))