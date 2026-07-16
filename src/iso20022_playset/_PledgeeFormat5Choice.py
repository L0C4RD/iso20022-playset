# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification80
from . import PledgeeTypeAndAnyBICIdentifier2
from . import PledgeeTypeAndText1

class PledgeeFormat5Choice(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Prtry", "_TpAndId"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PledgeeTypeAndText1, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PledgeeTypeAndText1, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification80, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification80, False)

	@property
	def TpAndId(self):
		return self._TpAndId

	@TpAndId.setter
	def TpAndId(self, value):
		self._TpAndId = value if value is not None else base_types.UninitialisedField(self, 'TpAndId', PledgeeTypeAndAnyBICIdentifier2, False)

	@TpAndId.deleter
	def TpAndId(self):
		del self._TpAndId
		self._TpAndId = base_types.UninitialisedField(self, 'TpAndId', PledgeeTypeAndAnyBICIdentifier2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PledgeeTypeAndText1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification80, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TpAndId', type=PledgeeTypeAndAnyBICIdentifier2, min=0, max=1, mutex_group=1, array=False),
	))