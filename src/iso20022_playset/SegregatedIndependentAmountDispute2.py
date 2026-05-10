import base_types
import Dispute1
import DisputeResolutionType1Choice

class SegregatedIndependentAmountDispute2(base_types._BaseFieldType):

	__slots__ = ["_DsptRsltnTp1Chc", "_DsptDtls"]
	@property
	def DsptRsltnTp1Chc(self):
		return self._DsptRsltnTp1Chc

	@DsptRsltnTp1Chc.setter
	def DsptRsltnTp1Chc(self, value):
		self._DsptRsltnTp1Chc = value if type(value) != auto else self.make_default("DsptRsltnTp1Chc")

	@DsptRsltnTp1Chc.deleter
	def DsptRsltnTp1Chc(self):
		del self._DsptRsltnTp1Chc
		self._DsptRsltnTp1Chc = None

	@property
	def DsptDtls(self):
		return self._DsptDtls

	@DsptDtls.setter
	def DsptDtls(self, value):
		self._DsptDtls = value if type(value) != auto else self.make_default("DsptDtls")

	@DsptDtls.deleter
	def DsptDtls(self):
		del self._DsptDtls
		self._DsptDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsptRsltnTp1Chc', type=DisputeResolutionType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DsptDtls', type=Dispute1, min=1, max=1, mutex_group=None, array=False),
	))

