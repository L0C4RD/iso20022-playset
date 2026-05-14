# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CancelledReason8Choice import CancelledReason8Choice
from ._Max210Text import Max210Text

class CancelledStatusReason11(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_RsnCd"]
	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if type(value) != base_types.auto else self.make_default("AddtlRsnInf")

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = None

	@property
	def RsnCd(self):
		return self._RsnCd

	@RsnCd.setter
	def RsnCd(self, value):
		self._RsnCd = value if type(value) != base_types.auto else self.make_default("RsnCd")

	@RsnCd.deleter
	def RsnCd(self):
		del self._RsnCd
		self._RsnCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsnCd', type=CancelledReason8Choice, min=1, max=1, mutex_group=None, array=False),
	))