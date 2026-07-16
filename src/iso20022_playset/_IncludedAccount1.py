# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import YesNoIndicator

class IncludedAccount1(base_types._BaseFieldType):

	__slots__ = ["_InclInd", "_SctiesAcctId"]
	@property
	def InclInd(self):
		return self._InclInd

	@InclInd.setter
	def InclInd(self, value):
		self._InclInd = value if value is not None else base_types.UninitialisedField(self, 'InclInd', YesNoIndicator, False)

	@InclInd.deleter
	def InclInd(self):
		del self._InclInd
		self._InclInd = base_types.UninitialisedField(self, 'InclInd', YesNoIndicator, False)

	@property
	def SctiesAcctId(self):
		return self._SctiesAcctId

	@SctiesAcctId.setter
	def SctiesAcctId(self, value):
		self._SctiesAcctId = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctId', Max35Text, False)

	@SctiesAcctId.deleter
	def SctiesAcctId(self):
		del self._SctiesAcctId
		self._SctiesAcctId = base_types.UninitialisedField(self, 'SctiesAcctId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InclInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))