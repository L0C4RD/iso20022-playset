import base_types
import Dispute1
import DisputeResolutionType2Choice

class VariationMarginDispute1(base_types._BaseFieldType):

	__slots__ = ["_RsltnTpDtls", "_DsptDtls"]
	@property
	def RsltnTpDtls(self):
		return self._RsltnTpDtls

	@RsltnTpDtls.setter
	def RsltnTpDtls(self, value):
		self._RsltnTpDtls = value if type(value) != auto else self.make_default("RsltnTpDtls")

	@RsltnTpDtls.deleter
	def RsltnTpDtls(self):
		del self._RsltnTpDtls
		self._RsltnTpDtls = None

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
		base_types.FieldEntry(name='RsltnTpDtls', type=DisputeResolutionType2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DsptDtls', type=Dispute1, min=1, max=1, mutex_group=None, array=False),
	))

