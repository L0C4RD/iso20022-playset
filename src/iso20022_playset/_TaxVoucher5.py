# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import RestrictedFINXMax16Text

class TaxVoucher5(base_types._BaseFieldType):

	__slots__ = ["_BrgnDt", "_BrgnSttlmDt", "_Id"]
	@property
	def BrgnDt(self):
		return self._BrgnDt

	@BrgnDt.setter
	def BrgnDt(self, value):
		self._BrgnDt = value if value is not None else base_types.UninitialisedField(self, 'BrgnDt', DateAndDateTime2Choice, False)

	@BrgnDt.deleter
	def BrgnDt(self):
		del self._BrgnDt
		self._BrgnDt = base_types.UninitialisedField(self, 'BrgnDt', DateAndDateTime2Choice, False)

	@property
	def BrgnSttlmDt(self):
		return self._BrgnSttlmDt

	@BrgnSttlmDt.setter
	def BrgnSttlmDt(self, value):
		self._BrgnSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'BrgnSttlmDt', DateAndDateTime2Choice, False)

	@BrgnSttlmDt.deleter
	def BrgnSttlmDt(self):
		del self._BrgnSttlmDt
		self._BrgnSttlmDt = base_types.UninitialisedField(self, 'BrgnSttlmDt', DateAndDateTime2Choice, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', RestrictedFINXMax16Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', RestrictedFINXMax16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BrgnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrgnSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
	))