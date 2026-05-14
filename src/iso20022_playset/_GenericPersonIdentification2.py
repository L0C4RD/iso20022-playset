# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._PersonIdentificationSchemeName1Choice import PersonIdentificationSchemeName1Choice

class GenericPersonIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Issr", "_SchmeNm"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

	@property
	def SchmeNm(self):
		return self._SchmeNm

	@SchmeNm.setter
	def SchmeNm(self, value):
		self._SchmeNm = value if type(value) != base_types.auto else self.make_default("SchmeNm")

	@SchmeNm.deleter
	def SchmeNm(self):
		del self._SchmeNm
		self._SchmeNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeNm', type=PersonIdentificationSchemeName1Choice, min=0, max=1, mutex_group=None, array=False),
	))