# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Dispute1
from . import DisputeResolutionType2Choice

class VariationMarginDispute1(base_types._BaseFieldType):

	__slots__ = ["_DsptDtls", "_RsltnTpDtls"]
	@property
	def DsptDtls(self):
		return self._DsptDtls

	@DsptDtls.setter
	def DsptDtls(self, value):
		self._DsptDtls = value if value is not None else base_types.UninitialisedField(self, 'DsptDtls', Dispute1, False)

	@DsptDtls.deleter
	def DsptDtls(self):
		del self._DsptDtls
		self._DsptDtls = base_types.UninitialisedField(self, 'DsptDtls', Dispute1, False)

	@property
	def RsltnTpDtls(self):
		return self._RsltnTpDtls

	@RsltnTpDtls.setter
	def RsltnTpDtls(self, value):
		self._RsltnTpDtls = value if value is not None else base_types.UninitialisedField(self, 'RsltnTpDtls', DisputeResolutionType2Choice, True)

	@RsltnTpDtls.deleter
	def RsltnTpDtls(self):
		del self._RsltnTpDtls
		self._RsltnTpDtls = base_types.UninitialisedField(self, 'RsltnTpDtls', DisputeResolutionType2Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsptDtls', type=Dispute1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltnTpDtls', type=DisputeResolutionType2Choice, min=0, max=None, mutex_group=None, array=True),
	))