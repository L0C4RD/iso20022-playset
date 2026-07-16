# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BlockedReason2Choice
from . import Max350Text
from . import TransactionType5Choice
from . import YesNoIndicator

class BlockedStatusReason2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Blckd", "_Rsn", "_TxTp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max350Text, False)

	@property
	def Blckd(self):
		return self._Blckd

	@Blckd.setter
	def Blckd(self, value):
		self._Blckd = value if value is not None else base_types.UninitialisedField(self, 'Blckd', YesNoIndicator, False)

	@Blckd.deleter
	def Blckd(self):
		del self._Blckd
		self._Blckd = base_types.UninitialisedField(self, 'Blckd', YesNoIndicator, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', BlockedReason2Choice, True)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', BlockedReason2Choice, True)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', TransactionType5Choice, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', TransactionType5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Blckd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=BlockedReason2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxTp', type=TransactionType5Choice, min=1, max=1, mutex_group=None, array=False),
	))