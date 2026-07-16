# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection102
from . import GenericIdentification165
from . import InitialMarginRequirement1

class EndOfDayRequirement2(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnRqrmnts", "_MrgnAcctId", "_VartnMrgnRqrmnts"]
	@property
	def InitlMrgnRqrmnts(self):
		return self._InitlMrgnRqrmnts

	@InitlMrgnRqrmnts.setter
	def InitlMrgnRqrmnts(self, value):
		self._InitlMrgnRqrmnts = value if value is not None else base_types.UninitialisedField(self, 'InitlMrgnRqrmnts', InitialMarginRequirement1, False)

	@InitlMrgnRqrmnts.deleter
	def InitlMrgnRqrmnts(self):
		del self._InitlMrgnRqrmnts
		self._InitlMrgnRqrmnts = base_types.UninitialisedField(self, 'InitlMrgnRqrmnts', InitialMarginRequirement1, False)

	@property
	def MrgnAcctId(self):
		return self._MrgnAcctId

	@MrgnAcctId.setter
	def MrgnAcctId(self, value):
		self._MrgnAcctId = value if value is not None else base_types.UninitialisedField(self, 'MrgnAcctId', GenericIdentification165, False)

	@MrgnAcctId.deleter
	def MrgnAcctId(self):
		del self._MrgnAcctId
		self._MrgnAcctId = base_types.UninitialisedField(self, 'MrgnAcctId', GenericIdentification165, False)

	@property
	def VartnMrgnRqrmnts(self):
		return self._VartnMrgnRqrmnts

	@VartnMrgnRqrmnts.setter
	def VartnMrgnRqrmnts(self, value):
		self._VartnMrgnRqrmnts = value if value is not None else base_types.UninitialisedField(self, 'VartnMrgnRqrmnts', AmountAndDirection102, False)

	@VartnMrgnRqrmnts.deleter
	def VartnMrgnRqrmnts(self):
		del self._VartnMrgnRqrmnts
		self._VartnMrgnRqrmnts = base_types.UninitialisedField(self, 'VartnMrgnRqrmnts', AmountAndDirection102, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnRqrmnts', type=InitialMarginRequirement1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnAcctId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VartnMrgnRqrmnts', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))