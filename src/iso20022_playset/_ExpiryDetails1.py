# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExpiryTerms1
from . import Max2000Text

class ExpiryDetails1(base_types._BaseFieldType):

	__slots__ = ["_AddtlXpryInf", "_XpryTerms"]
	@property
	def AddtlXpryInf(self):
		return self._AddtlXpryInf

	@AddtlXpryInf.setter
	def AddtlXpryInf(self, value):
		self._AddtlXpryInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlXpryInf', Max2000Text, True)

	@AddtlXpryInf.deleter
	def AddtlXpryInf(self):
		del self._AddtlXpryInf
		self._AddtlXpryInf = base_types.UninitialisedField(self, 'AddtlXpryInf', Max2000Text, True)

	@property
	def XpryTerms(self):
		return self._XpryTerms

	@XpryTerms.setter
	def XpryTerms(self, value):
		self._XpryTerms = value if value is not None else base_types.UninitialisedField(self, 'XpryTerms', ExpiryTerms1, False)

	@XpryTerms.deleter
	def XpryTerms(self):
		del self._XpryTerms
		self._XpryTerms = base_types.UninitialisedField(self, 'XpryTerms', ExpiryTerms1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlXpryInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='XpryTerms', type=ExpiryTerms1, min=0, max=1, mutex_group=None, array=False),
	))