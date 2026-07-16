# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddressType1Code
from . import NameAndAddress4
from . import YesNoIndicator

class PostalAddress3(base_types._BaseFieldType):

	__slots__ = ["_AdrTp", "_MlngInd", "_NmAndAdr", "_RegnAdrInd"]
	@property
	def AdrTp(self):
		return self._AdrTp

	@AdrTp.setter
	def AdrTp(self, value):
		self._AdrTp = value if value is not None else base_types.UninitialisedField(self, 'AdrTp', AddressType1Code, False)

	@AdrTp.deleter
	def AdrTp(self):
		del self._AdrTp
		self._AdrTp = base_types.UninitialisedField(self, 'AdrTp', AddressType1Code, False)

	@property
	def MlngInd(self):
		return self._MlngInd

	@MlngInd.setter
	def MlngInd(self, value):
		self._MlngInd = value if value is not None else base_types.UninitialisedField(self, 'MlngInd', YesNoIndicator, False)

	@MlngInd.deleter
	def MlngInd(self):
		del self._MlngInd
		self._MlngInd = base_types.UninitialisedField(self, 'MlngInd', YesNoIndicator, False)

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if value is not None else base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress4, False)

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = base_types.UninitialisedField(self, 'NmAndAdr', NameAndAddress4, False)

	@property
	def RegnAdrInd(self):
		return self._RegnAdrInd

	@RegnAdrInd.setter
	def RegnAdrInd(self, value):
		self._RegnAdrInd = value if value is not None else base_types.UninitialisedField(self, 'RegnAdrInd', YesNoIndicator, False)

	@RegnAdrInd.deleter
	def RegnAdrInd(self):
		del self._RegnAdrInd
		self._RegnAdrInd = base_types.UninitialisedField(self, 'RegnAdrInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrTp', type=AddressType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAdrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))