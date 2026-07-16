# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AttestationValue1Code
from . import Exemption2
from . import Max4Text
from . import TrueFalseIndicator

class StrongCustomerAuthentication2(base_types._BaseFieldType):

	__slots__ = ["_DlgtdAuthrty", "_RsnAuthntcnNotPrfrmd", "_SbjtToSCA", "_Wvr", "_Xmptn"]
	@property
	def DlgtdAuthrty(self):
		return self._DlgtdAuthrty

	@DlgtdAuthrty.setter
	def DlgtdAuthrty(self, value):
		self._DlgtdAuthrty = value if value is not None else base_types.UninitialisedField(self, 'DlgtdAuthrty', AttestationValue1Code, False)

	@DlgtdAuthrty.deleter
	def DlgtdAuthrty(self):
		del self._DlgtdAuthrty
		self._DlgtdAuthrty = base_types.UninitialisedField(self, 'DlgtdAuthrty', AttestationValue1Code, False)

	@property
	def RsnAuthntcnNotPrfrmd(self):
		return self._RsnAuthntcnNotPrfrmd

	@RsnAuthntcnNotPrfrmd.setter
	def RsnAuthntcnNotPrfrmd(self, value):
		self._RsnAuthntcnNotPrfrmd = value if value is not None else base_types.UninitialisedField(self, 'RsnAuthntcnNotPrfrmd', Max4Text, False)

	@RsnAuthntcnNotPrfrmd.deleter
	def RsnAuthntcnNotPrfrmd(self):
		del self._RsnAuthntcnNotPrfrmd
		self._RsnAuthntcnNotPrfrmd = base_types.UninitialisedField(self, 'RsnAuthntcnNotPrfrmd', Max4Text, False)

	@property
	def SbjtToSCA(self):
		return self._SbjtToSCA

	@SbjtToSCA.setter
	def SbjtToSCA(self, value):
		self._SbjtToSCA = value if value is not None else base_types.UninitialisedField(self, 'SbjtToSCA', TrueFalseIndicator, False)

	@SbjtToSCA.deleter
	def SbjtToSCA(self):
		del self._SbjtToSCA
		self._SbjtToSCA = base_types.UninitialisedField(self, 'SbjtToSCA', TrueFalseIndicator, False)

	@property
	def Wvr(self):
		return self._Wvr

	@Wvr.setter
	def Wvr(self, value):
		self._Wvr = value if value is not None else base_types.UninitialisedField(self, 'Wvr', AttestationValue1Code, False)

	@Wvr.deleter
	def Wvr(self):
		del self._Wvr
		self._Wvr = base_types.UninitialisedField(self, 'Wvr', AttestationValue1Code, False)

	@property
	def Xmptn(self):
		return self._Xmptn

	@Xmptn.setter
	def Xmptn(self, value):
		self._Xmptn = value if value is not None else base_types.UninitialisedField(self, 'Xmptn', Exemption2, True)

	@Xmptn.deleter
	def Xmptn(self):
		del self._Xmptn
		self._Xmptn = base_types.UninitialisedField(self, 'Xmptn', Exemption2, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlgtdAuthrty', type=AttestationValue1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsnAuthntcnNotPrfrmd', type=Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtToSCA', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Wvr', type=AttestationValue1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xmptn', type=Exemption2, min=0, max=None, mutex_group=None, array=True),
	))