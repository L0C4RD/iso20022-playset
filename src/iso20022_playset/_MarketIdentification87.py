# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClassificationType1Choice
from . import CountryCode
from . import Purpose3Choice

class MarketIdentification87(base_types._BaseFieldType):

	__slots__ = ["_ClssfctnTp", "_Ctry", "_SttlmPurp"]
	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType1Choice, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType1Choice, False)

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def SttlmPurp(self):
		return self._SttlmPurp

	@SttlmPurp.setter
	def SttlmPurp(self, value):
		self._SttlmPurp = value if value is not None else base_types.UninitialisedField(self, 'SttlmPurp', Purpose3Choice, False)

	@SttlmPurp.deleter
	def SttlmPurp(self):
		del self._SttlmPurp
		self._SttlmPurp = base_types.UninitialisedField(self, 'SttlmPurp', Purpose3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPurp', type=Purpose3Choice, min=0, max=1, mutex_group=None, array=False),
	))