from . import base_types
import PartyIdentification25
import CashAccount7

class PartyIdentificationAndAccount6(base_types._BaseFieldType):

	__slots__ = ["_FincgAcct", "_CdtAcct", "_PtyId"]
	@property
	def FincgAcct(self):
		return self._FincgAcct

	@FincgAcct.setter
	def FincgAcct(self, value):
		self._FincgAcct = value if type(value) != auto else self.make_default("FincgAcct")

	@FincgAcct.deleter
	def FincgAcct(self):
		del self._FincgAcct
		self._FincgAcct = None

	@property
	def CdtAcct(self):
		return self._CdtAcct

	@CdtAcct.setter
	def CdtAcct(self, value):
		self._CdtAcct = value if type(value) != auto else self.make_default("CdtAcct")

	@CdtAcct.deleter
	def CdtAcct(self):
		del self._CdtAcct
		self._CdtAcct = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FincgAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification25, min=1, max=1, mutex_group=None, array=False),
	))

