# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import RejectedReason29Choice

class RejectedStatusReason28(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_RsnCd"]
	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlRsnInf', Max350Text, False)

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = base_types.UninitialisedField(self, 'AddtlRsnInf', Max350Text, False)

	@property
	def RsnCd(self):
		return self._RsnCd

	@RsnCd.setter
	def RsnCd(self, value):
		self._RsnCd = value if value is not None else base_types.UninitialisedField(self, 'RsnCd', RejectedReason29Choice, False)

	@RsnCd.deleter
	def RsnCd(self):
		del self._RsnCd
		self._RsnCd = base_types.UninitialisedField(self, 'RsnCd', RejectedReason29Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsnCd', type=RejectedReason29Choice, min=1, max=1, mutex_group=None, array=False),
	))