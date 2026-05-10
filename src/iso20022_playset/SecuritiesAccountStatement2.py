from . import base_types
import ISODate
import SecuritiesAccountReferenceDataChange2

class SecuritiesAccountStatement2(base_types._BaseFieldType):

	__slots__ = ["_Chng", "_SysDt"]
	@property
	def Chng(self):
		return self._Chng

	@Chng.setter
	def Chng(self, value):
		self._Chng = value if type(value) != auto else self.make_default("Chng")

	@Chng.deleter
	def Chng(self):
		del self._Chng
		self._Chng = None

	@property
	def SysDt(self):
		return self._SysDt

	@SysDt.setter
	def SysDt(self, value):
		self._SysDt = value if type(value) != auto else self.make_default("SysDt")

	@SysDt.deleter
	def SysDt(self):
		del self._SysDt
		self._SysDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chng', type=SecuritiesAccountReferenceDataChange2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

