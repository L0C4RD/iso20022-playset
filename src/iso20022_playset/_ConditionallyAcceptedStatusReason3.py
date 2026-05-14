# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ConditionallyAcceptedStatusReason3Choice import ConditionallyAcceptedStatusReason3Choice
from ._Max350Text import Max350Text

class ConditionallyAcceptedStatusReason3(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Rsn"]
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

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=ConditionallyAcceptedStatusReason3Choice, min=1, max=1, mutex_group=None, array=False),
	))