# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max2000Text

class BankInstructions1(base_types._BaseFieldType):

	__slots__ = ["_LastDtForRspn", "_Txt"]
	@property
	def LastDtForRspn(self):
		return self._LastDtForRspn

	@LastDtForRspn.setter
	def LastDtForRspn(self, value):
		self._LastDtForRspn = value if value is not None else base_types.UninitialisedField(self, 'LastDtForRspn', ISODate, False)

	@LastDtForRspn.deleter
	def LastDtForRspn(self):
		del self._LastDtForRspn
		self._LastDtForRspn = base_types.UninitialisedField(self, 'LastDtForRspn', ISODate, False)

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if value is not None else base_types.UninitialisedField(self, 'Txt', Max2000Text, True)

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = base_types.UninitialisedField(self, 'Txt', Max2000Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LastDtForRspn', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Txt', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))