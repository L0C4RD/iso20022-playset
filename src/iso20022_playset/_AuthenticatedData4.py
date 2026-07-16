# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlgorithmIdentification15
from . import EncapsulatedContent3
from . import Max140Binary
from . import Number
from . import Recipient4Choice

class AuthenticatedData4(base_types._BaseFieldType):

	__slots__ = ["_MAC", "_MACAlgo", "_NcpsltdCntt", "_Rcpt", "_Vrsn"]
	@property
	def MAC(self):
		return self._MAC

	@MAC.setter
	def MAC(self, value):
		self._MAC = value if value is not None else base_types.UninitialisedField(self, 'MAC', Max140Binary, False)

	@MAC.deleter
	def MAC(self):
		del self._MAC
		self._MAC = base_types.UninitialisedField(self, 'MAC', Max140Binary, False)

	@property
	def MACAlgo(self):
		return self._MACAlgo

	@MACAlgo.setter
	def MACAlgo(self, value):
		self._MACAlgo = value if value is not None else base_types.UninitialisedField(self, 'MACAlgo', AlgorithmIdentification15, False)

	@MACAlgo.deleter
	def MACAlgo(self):
		del self._MACAlgo
		self._MACAlgo = base_types.UninitialisedField(self, 'MACAlgo', AlgorithmIdentification15, False)

	@property
	def NcpsltdCntt(self):
		return self._NcpsltdCntt

	@NcpsltdCntt.setter
	def NcpsltdCntt(self, value):
		self._NcpsltdCntt = value if value is not None else base_types.UninitialisedField(self, 'NcpsltdCntt', EncapsulatedContent3, False)

	@NcpsltdCntt.deleter
	def NcpsltdCntt(self):
		del self._NcpsltdCntt
		self._NcpsltdCntt = base_types.UninitialisedField(self, 'NcpsltdCntt', EncapsulatedContent3, False)

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', Recipient4Choice, True)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', Recipient4Choice, True)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Number, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MAC', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MACAlgo', type=AlgorithmIdentification15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcpsltdCntt', type=EncapsulatedContent3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=Recipient4Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))