from . import base_types
from ._AddressType1Code import AddressType1Code
from ._NameAndAddress4 import NameAndAddress4
from ._YesNoIndicator import YesNoIndicator

class PostalAddress3(base_types._BaseFieldType):

	__slots__ = ["_AdrTp", "_MlngInd", "_NmAndAdr", "_RegnAdrInd"]
	@property
	def AdrTp(self):
		return self._AdrTp

	@AdrTp.setter
	def AdrTp(self, value):
		self._AdrTp = value if type(value) != base_types.auto else self.make_default("AdrTp")

	@AdrTp.deleter
	def AdrTp(self):
		del self._AdrTp
		self._AdrTp = None

	@property
	def MlngInd(self):
		return self._MlngInd

	@MlngInd.setter
	def MlngInd(self, value):
		self._MlngInd = value if type(value) != base_types.auto else self.make_default("MlngInd")

	@MlngInd.deleter
	def MlngInd(self):
		del self._MlngInd
		self._MlngInd = None

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != base_types.auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	@property
	def RegnAdrInd(self):
		return self._RegnAdrInd

	@RegnAdrInd.setter
	def RegnAdrInd(self, value):
		self._RegnAdrInd = value if type(value) != base_types.auto else self.make_default("RegnAdrInd")

	@RegnAdrInd.deleter
	def RegnAdrInd(self):
		del self._RegnAdrInd
		self._RegnAdrInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrTp', type=AddressType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MlngInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAdrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

