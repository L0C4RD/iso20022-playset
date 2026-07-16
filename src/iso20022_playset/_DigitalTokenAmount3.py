# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DTI2024Identifier
from . import Max30DecimalNumber
from . import Max30Text

class DigitalTokenAmount3(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Idr", "_Unit"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max30Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max30Text, False)

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if value is not None else base_types.UninitialisedField(self, 'Idr', DTI2024Identifier, False)

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = base_types.UninitialisedField(self, 'Idr', DTI2024Identifier, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', Max30DecimalNumber, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', Max30DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max30Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=DTI2024Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=Max30DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))