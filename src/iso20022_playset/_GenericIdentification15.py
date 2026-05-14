# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._Max4AlphaNumericText import Max4AlphaNumericText
from ._Number import Number

class GenericIdentification15(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_Id", "_Issr", "_SchmeNm"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

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
		base_types.FieldEntry(name='Bal', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))