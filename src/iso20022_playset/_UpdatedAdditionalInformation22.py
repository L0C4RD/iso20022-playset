# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._RestrictedFINXMax350Text import RestrictedFINXMax350Text

class UpdatedAdditionalInformation22(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=RestrictedFINXMax350Text, min=1, max=1, mutex_group=None, array=False),
	))