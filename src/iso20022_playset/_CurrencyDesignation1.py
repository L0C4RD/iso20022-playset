# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CountryCode import CountryCode
from ._CurrencyDesignation1Code import CurrencyDesignation1Code
from ._Max350Text import Max350Text

class CurrencyDesignation1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CcyDsgnt", "_Lctn"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CcyDsgnt(self):
		return self._CcyDsgnt

	@CcyDsgnt.setter
	def CcyDsgnt(self, value):
		self._CcyDsgnt = value if type(value) != base_types.auto else self.make_default("CcyDsgnt")

	@CcyDsgnt.deleter
	def CcyDsgnt(self):
		del self._CcyDsgnt
		self._CcyDsgnt = None

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != base_types.auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyDsgnt', type=CurrencyDesignation1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))