# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DisputeNotification2 import DisputeNotification2
from ._SegregatedIndependentAmountDispute2 import SegregatedIndependentAmountDispute2

class DisputeNotification2Choice(base_types._BaseFieldType):

	__slots__ = ["_DsptNtfctnDtls", "_SgrtdIndpdntAmtDsptDtls"]
	@property
	def DsptNtfctnDtls(self):
		return self._DsptNtfctnDtls

	@DsptNtfctnDtls.setter
	def DsptNtfctnDtls(self, value):
		self._DsptNtfctnDtls = value if type(value) != base_types.auto else self.make_default("DsptNtfctnDtls")

	@DsptNtfctnDtls.deleter
	def DsptNtfctnDtls(self):
		del self._DsptNtfctnDtls
		self._DsptNtfctnDtls = None

	@property
	def SgrtdIndpdntAmtDsptDtls(self):
		return self._SgrtdIndpdntAmtDsptDtls

	@SgrtdIndpdntAmtDsptDtls.setter
	def SgrtdIndpdntAmtDsptDtls(self, value):
		self._SgrtdIndpdntAmtDsptDtls = value if type(value) != base_types.auto else self.make_default("SgrtdIndpdntAmtDsptDtls")

	@SgrtdIndpdntAmtDsptDtls.deleter
	def SgrtdIndpdntAmtDsptDtls(self):
		del self._SgrtdIndpdntAmtDsptDtls
		self._SgrtdIndpdntAmtDsptDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsptNtfctnDtls', type=DisputeNotification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmtDsptDtls', type=SegregatedIndependentAmountDispute2, min=0, max=1, mutex_group=1, array=False),
	))