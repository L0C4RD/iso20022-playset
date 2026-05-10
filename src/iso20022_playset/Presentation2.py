import base_types
import PartyIdentification43
import ISODate

class Presentation2(base_types._BaseFieldType):

	__slots__ = ["_Presntr", "_BnfcryPresntnDt"]
	@property
	def Presntr(self):
		return self._Presntr

	@Presntr.setter
	def Presntr(self, value):
		self._Presntr = value if type(value) != auto else self.make_default("Presntr")

	@Presntr.deleter
	def Presntr(self):
		del self._Presntr
		self._Presntr = None

	@property
	def BnfcryPresntnDt(self):
		return self._BnfcryPresntnDt

	@BnfcryPresntnDt.setter
	def BnfcryPresntnDt(self, value):
		self._BnfcryPresntnDt = value if type(value) != auto else self.make_default("BnfcryPresntnDt")

	@BnfcryPresntnDt.deleter
	def BnfcryPresntnDt(self):
		del self._BnfcryPresntnDt
		self._BnfcryPresntnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Presntr', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryPresntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

