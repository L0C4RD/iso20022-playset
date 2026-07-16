# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType39
from . import Max100KBinary
from . import Max1025Text

class ExternallyDefinedData5(base_types._BaseFieldType):

	__slots__ = ["_Id", "_PrtctdVal", "_Tp", "_Val"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max1025Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max1025Text, False)

	@property
	def PrtctdVal(self):
		return self._PrtctdVal

	@PrtctdVal.setter
	def PrtctdVal(self, value):
		self._PrtctdVal = value if value is not None else base_types.UninitialisedField(self, 'PrtctdVal', ContentInformationType39, False)

	@PrtctdVal.deleter
	def PrtctdVal(self):
		del self._PrtctdVal
		self._PrtctdVal = base_types.UninitialisedField(self, 'PrtctdVal', ContentInformationType39, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max1025Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max1025Text, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max100KBinary, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max100KBinary, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max1025Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdVal', type=ContentInformationType39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
	))