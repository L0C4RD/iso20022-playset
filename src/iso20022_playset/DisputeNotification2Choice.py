import base_types
import SegregatedIndependentAmountDispute2
import DisputeNotification2

class DisputeNotification2Choice(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmtDsptDtls", "_DsptNtfctnDtls"]
	@property
	def SgrtdIndpdntAmtDsptDtls(self):
		return self._SgrtdIndpdntAmtDsptDtls

	@SgrtdIndpdntAmtDsptDtls.setter
	def SgrtdIndpdntAmtDsptDtls(self, value):
		self._SgrtdIndpdntAmtDsptDtls = value if type(value) != auto else self.make_default("SgrtdIndpdntAmtDsptDtls")

	@SgrtdIndpdntAmtDsptDtls.deleter
	def SgrtdIndpdntAmtDsptDtls(self):
		del self._SgrtdIndpdntAmtDsptDtls
		self._SgrtdIndpdntAmtDsptDtls = None

	@property
	def DsptNtfctnDtls(self):
		return self._DsptNtfctnDtls

	@DsptNtfctnDtls.setter
	def DsptNtfctnDtls(self, value):
		self._DsptNtfctnDtls = value if type(value) != auto else self.make_default("DsptNtfctnDtls")

	@DsptNtfctnDtls.deleter
	def DsptNtfctnDtls(self):
		del self._DsptNtfctnDtls
		self._DsptNtfctnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmtDsptDtls', type=SegregatedIndependentAmountDispute2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DsptNtfctnDtls', type=DisputeNotification2, min=0, max=1, mutex_group=1, array=False),
	))

