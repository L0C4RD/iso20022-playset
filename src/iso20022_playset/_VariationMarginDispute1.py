# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Dispute1 import Dispute1
from ._DisputeResolutionType2Choice import DisputeResolutionType2Choice

class VariationMarginDispute1(base_types._BaseFieldType):

	__slots__ = ["_DsptDtls", "_RsltnTpDtls"]
	@property
	def DsptDtls(self):
		return self._DsptDtls

	@DsptDtls.setter
	def DsptDtls(self, value):
		self._DsptDtls = value if type(value) != base_types.auto else self.make_default("DsptDtls")

	@DsptDtls.deleter
	def DsptDtls(self):
		del self._DsptDtls
		self._DsptDtls = None

	@property
	def RsltnTpDtls(self):
		return self._RsltnTpDtls

	@RsltnTpDtls.setter
	def RsltnTpDtls(self, value):
		self._RsltnTpDtls = value if type(value) != base_types.auto else self.make_default("RsltnTpDtls")

	@RsltnTpDtls.deleter
	def RsltnTpDtls(self):
		del self._RsltnTpDtls
		self._RsltnTpDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DsptDtls', type=Dispute1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltnTpDtls', type=DisputeResolutionType2Choice, min=0, max=None, mutex_group=None, array=True),
	))