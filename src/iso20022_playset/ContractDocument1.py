import base_types
import ISODate
import Max35Text
import Max6Text

class ContractDocument1(base_types._BaseFieldType):

	__slots__ = ["_Vrsn", "_SgnOffDt", "_Ref"]
	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def SgnOffDt(self):
		return self._SgnOffDt

	@SgnOffDt.setter
	def SgnOffDt(self, value):
		self._SgnOffDt = value if type(value) != auto else self.make_default("SgnOffDt")

	@SgnOffDt.deleter
	def SgnOffDt(self):
		del self._SgnOffDt
		self._SgnOffDt = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Vrsn', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgnOffDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

