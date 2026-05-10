from . import base_types
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text

class TaxVoucher5(base_types._BaseFieldType):

	__slots__ = ["_Id", "_BrgnDt", "_BrgnSttlmDt"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def BrgnDt(self):
		return self._BrgnDt

	@BrgnDt.setter
	def BrgnDt(self, value):
		self._BrgnDt = value if type(value) != base_types.auto else self.make_default("BrgnDt")

	@BrgnDt.deleter
	def BrgnDt(self):
		del self._BrgnDt
		self._BrgnDt = None

	@property
	def BrgnSttlmDt(self):
		return self._BrgnSttlmDt

	@BrgnSttlmDt.setter
	def BrgnSttlmDt(self, value):
		self._BrgnSttlmDt = value if type(value) != base_types.auto else self.make_default("BrgnSttlmDt")

	@BrgnSttlmDt.deleter
	def BrgnSttlmDt(self):
		del self._BrgnSttlmDt
		self._BrgnSttlmDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrgnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrgnSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

