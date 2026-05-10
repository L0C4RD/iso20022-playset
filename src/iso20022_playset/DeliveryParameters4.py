import base_types
import ContactIdentification2
import NameAndAddress4
import YesNoIndicator

class DeliveryParameters4(base_types._BaseFieldType):

	__slots__ = ["_CtctPrsn", "_RegdAdrInd", "_NmAndAdr"]
	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if type(value) != auto else self.make_default("CtctPrsn")

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = None

	@property
	def RegdAdrInd(self):
		return self._RegdAdrInd

	@RegdAdrInd.setter
	def RegdAdrInd(self, value):
		self._RegdAdrInd = value if type(value) != auto else self.make_default("RegdAdrInd")

	@RegdAdrInd.deleter
	def RegdAdrInd(self):
		del self._RegdAdrInd
		self._RegdAdrInd = None

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdAdrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress4, min=0, max=1, mutex_group=None, array=False),
	))

