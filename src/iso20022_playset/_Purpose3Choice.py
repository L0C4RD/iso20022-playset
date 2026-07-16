# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalSecuritiesPurpose1Code
from . import GenericIdentification1

class Purpose3Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_SctiesPurpCd"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification1, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification1, False)

	@property
	def SctiesPurpCd(self):
		return self._SctiesPurpCd

	@SctiesPurpCd.setter
	def SctiesPurpCd(self, value):
		self._SctiesPurpCd = value if value is not None else base_types.UninitialisedField(self, 'SctiesPurpCd', ExternalSecuritiesPurpose1Code, False)

	@SctiesPurpCd.deleter
	def SctiesPurpCd(self):
		del self._SctiesPurpCd
		self._SctiesPurpCd = base_types.UninitialisedField(self, 'SctiesPurpCd', ExternalSecuritiesPurpose1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesPurpCd', type=ExternalSecuritiesPurpose1Code, min=0, max=1, mutex_group=1, array=False),
	))