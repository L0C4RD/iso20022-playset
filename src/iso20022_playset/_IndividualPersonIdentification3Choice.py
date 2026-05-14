# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GenericIdentification81 import GenericIdentification81
from ._IndividualPerson35 import IndividualPerson35

class IndividualPersonIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_IdNb", "_PrsnNm"]
	@property
	def IdNb(self):
		return self._IdNb

	@IdNb.setter
	def IdNb(self, value):
		self._IdNb = value if type(value) != base_types.auto else self.make_default("IdNb")

	@IdNb.deleter
	def IdNb(self):
		del self._IdNb
		self._IdNb = None

	@property
	def PrsnNm(self):
		return self._PrsnNm

	@PrsnNm.setter
	def PrsnNm(self, value):
		self._PrsnNm = value if type(value) != base_types.auto else self.make_default("PrsnNm")

	@PrsnNm.deleter
	def PrsnNm(self):
		del self._PrsnNm
		self._PrsnNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdNb', type=GenericIdentification81, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrsnNm', type=IndividualPerson35, min=0, max=1, mutex_group=1, array=False),
	))