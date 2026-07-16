# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DisputeNotification2
from . import SegregatedIndependentAmountDispute2

class DisputeNotification2Choice(base_types._BaseFieldType):

	__slots__ = ["_DsptNtfctnDtls", "_SgrtdIndpdntAmtDsptDtls"]
	@property
	def DsptNtfctnDtls(self):
		return self._DsptNtfctnDtls

	@DsptNtfctnDtls.setter
	def DsptNtfctnDtls(self, value):
		self._DsptNtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'DsptNtfctnDtls', DisputeNotification2, False)

	@DsptNtfctnDtls.deleter
	def DsptNtfctnDtls(self):
		del self._DsptNtfctnDtls
		self._DsptNtfctnDtls = base_types.UninitialisedField(self, 'DsptNtfctnDtls', DisputeNotification2, False)

	@property
	def SgrtdIndpdntAmtDsptDtls(self):
		return self._SgrtdIndpdntAmtDsptDtls

	@SgrtdIndpdntAmtDsptDtls.setter
	def SgrtdIndpdntAmtDsptDtls(self, value):
		self._SgrtdIndpdntAmtDsptDtls = value if value is not None else base_types.UninitialisedField(self, 'SgrtdIndpdntAmtDsptDtls', SegregatedIndependentAmountDispute2, False)

	@SgrtdIndpdntAmtDsptDtls.deleter
	def SgrtdIndpdntAmtDsptDtls(self):
		del self._SgrtdIndpdntAmtDsptDtls
		self._SgrtdIndpdntAmtDsptDtls = base_types.UninitialisedField(self, 'SgrtdIndpdntAmtDsptDtls', SegregatedIndependentAmountDispute2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsptNtfctnDtls', type=DisputeNotification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmtDsptDtls', type=SegregatedIndependentAmountDispute2, min=0, max=1, mutex_group=1, array=False),
	))