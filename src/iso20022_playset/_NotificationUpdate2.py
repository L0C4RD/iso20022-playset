# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import YesNoIndicator

class NotificationUpdate2(base_types._BaseFieldType):

	__slots__ = ["_PrvsNtfctnId", "_RcnfrmInstrs"]
	@property
	def PrvsNtfctnId(self):
		return self._PrvsNtfctnId

	@PrvsNtfctnId.setter
	def PrvsNtfctnId(self, value):
		self._PrvsNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'PrvsNtfctnId', Max35Text, False)

	@PrvsNtfctnId.deleter
	def PrvsNtfctnId(self):
		del self._PrvsNtfctnId
		self._PrvsNtfctnId = base_types.UninitialisedField(self, 'PrvsNtfctnId', Max35Text, False)

	@property
	def RcnfrmInstrs(self):
		return self._RcnfrmInstrs

	@RcnfrmInstrs.setter
	def RcnfrmInstrs(self, value):
		self._RcnfrmInstrs = value if value is not None else base_types.UninitialisedField(self, 'RcnfrmInstrs', YesNoIndicator, False)

	@RcnfrmInstrs.deleter
	def RcnfrmInstrs(self):
		del self._RcnfrmInstrs
		self._RcnfrmInstrs = base_types.UninitialisedField(self, 'RcnfrmInstrs', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvsNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcnfrmInstrs', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))