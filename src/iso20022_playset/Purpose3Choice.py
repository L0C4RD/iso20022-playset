import base_types
import ExternalSecuritiesPurpose1Code
import GenericIdentification1

class Purpose3Choice(base_types._BaseFieldType):

	__slots__ = ["_SctiesPurpCd", "_Prtry"]
	@property
	def SctiesPurpCd(self):
		return self._SctiesPurpCd

	@SctiesPurpCd.setter
	def SctiesPurpCd(self, value):
		self._SctiesPurpCd = value if type(value) != auto else self.make_default("SctiesPurpCd")

	@SctiesPurpCd.deleter
	def SctiesPurpCd(self):
		del self._SctiesPurpCd
		self._SctiesPurpCd = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesPurpCd', type=ExternalSecuritiesPurpose1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

