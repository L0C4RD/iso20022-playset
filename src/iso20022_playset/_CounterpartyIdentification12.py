# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Branch6Choice
from . import CountryCode
from . import PartyIdentification236Choice

class CounterpartyIdentification12(base_types._BaseFieldType):

	__slots__ = ["_Brnch", "_CtryCd", "_Id"]
	@property
	def Brnch(self):
		return self._Brnch

	@Brnch.setter
	def Brnch(self, value):
		self._Brnch = value if value is not None else base_types.UninitialisedField(self, 'Brnch', Branch6Choice, False)

	@Brnch.deleter
	def Brnch(self):
		del self._Brnch
		self._Brnch = base_types.UninitialisedField(self, 'Brnch', Branch6Choice, False)

	@property
	def CtryCd(self):
		return self._CtryCd

	@CtryCd.setter
	def CtryCd(self, value):
		self._CtryCd = value if value is not None else base_types.UninitialisedField(self, 'CtryCd', CountryCode, False)

	@CtryCd.deleter
	def CtryCd(self):
		del self._CtryCd
		self._CtryCd = base_types.UninitialisedField(self, 'CtryCd', CountryCode, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification236Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification236Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Brnch', type=Branch6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryCd', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification236Choice, min=1, max=1, mutex_group=None, array=False),
	))