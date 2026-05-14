# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._SecurityIdentification19 import SecurityIdentification19
from ._SecurityInstrumentDescription22 import SecurityInstrumentDescription22

class FinancialInstrumentAttributes5Choice(base_types._BaseFieldType):

	__slots__ = ["_AltrnId", "_Id", "_Othr"]
	@property
	def AltrnId(self):
		return self._AltrnId

	@AltrnId.setter
	def AltrnId(self, value):
		self._AltrnId = value if type(value) != base_types.auto else self.make_default("AltrnId")

	@AltrnId.deleter
	def AltrnId(self):
		del self._AltrnId
		self._AltrnId = None

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
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnId', type=SecurityIdentification19, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=SecurityInstrumentDescription22, min=0, max=1, mutex_group=1, array=False),
	))