# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Reason20Choice import Reason20Choice
from ._SecurityIdentification20 import SecurityIdentification20
from ._Status22Choice import Status22Choice

class AdditionalQueryParameters14(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_Rsn", "_Sts"]
	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

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

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rsn', type=Reason20Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=Status22Choice, min=0, max=1, mutex_group=None, array=False),
	))